

                package com.example.tests;

        import com.example.utils.DatabaseUtil;
        import com.example.pages.TodoPage;
        import org.junit.jupiter.api.*;
        import org.openqa.selenium.*;
        import org.openqa.selenium.chrome.ChromeDriver;
        import org.openqa.selenium.chrome.ChromeDriverService;
        import org.openqa.selenium.chrome.ChromeOptions;
        import org.openqa.selenium.support.ui.ExpectedConditions;
        import org.openqa.selenium.support.ui.WebDriverWait;
        import java.sql.Connection;
        import java.sql.PreparedStatement;
        import java.sql.ResultSet;
        import java.sql.SQLException;
        import java.time.Duration;
        import static org.junit.jupiter.api.Assertions.assertTrue;

        public class TodoUITest {
            private static WebDriver driver;
            private Connection conn;
            private TodoPage todoPage;

            @BeforeAll
            public static void setupClass() {
                // Automatically set up the correct version of ChromeDriver using WebDriverManager
//                System.setProperty("webdriver.chrome.driver", "/Users/timmeshk/Downloads/chromedriverV3/chromedriver"); // Specify the full path here
            }

            @BeforeEach
            public void setupTest() throws SQLException {
                // Set up Chrome options for proper handling
                ChromeOptions options = new ChromeOptions();
                options.addArguments("--allow-file-access-from-files");
                options.addArguments("--headless");  // Enable headless mode
                options.addArguments("--disable-web-security");
                options.addArguments("--allow-insecure-localhost");
                options.addArguments("--remote-allow-origins=*");

                // Initialize the ChromeDriver with options
                ChromeDriverService service = new ChromeDriverService.Builder()
                        .usingPort(9515)
                        .build();
                WebDriver driver = new ChromeDriver(service, options);
                // **Load the deployed ToDo app at http://localhost:8081/**
                String appUrl = "http://localhost:8081/";
                driver.get(appUrl);

                // Wait for the todo-input field to be visible before interacting
                WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
                WebElement todoInput = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("todo-input")));

                conn = DatabaseUtil.getConnection();
                todoPage = new TodoPage(driver);
            }

            @Test
            public void testAddTodo() throws SQLException {
                // Wait for the todo-input field to be visible
                WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
                WebElement todoInput = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("todo-input")));

                todoInput.sendKeys("Automated Task");
                driver.findElement(By.id("add-btn")).click(); // Adjust based on your app's button ID

                // Validate in UI
                assertTrue(todoPage.isTodoPresent("Automated Task"));

                // Validate in Database
                PreparedStatement checkStmt = conn.prepareStatement("SELECT * FROM todos WHERE title='Automated Task'");
                ResultSet rs = checkStmt.executeQuery();
                assertTrue(rs.next(), "Task was not added to the database.");
            }

//            @Test
            public void testUpdateTodo() throws SQLException {
                // Wait for edit button to be visible and interact with it
                WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
                WebElement editButton = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("edit-btn-1")));
                editButton.click();

                WebElement editField = driver.findElement(By.id("edit-input-1"));
                editField.clear();
                editField.sendKeys("Updated Task");
                driver.findElement(By.id("save-btn-1")).click();

                // Validate the UI update
                assertTrue(driver.getPageSource().contains("Updated Task"));

                // Validate in Database
                PreparedStatement checkStmt = conn.prepareStatement("SELECT * FROM todos WHERE title='Updated Task'");
                ResultSet rs = checkStmt.executeQuery();
                assertTrue(rs.next(), "Task was not updated in the database.");
            }

//            @Test
            public void testDeleteTodo() throws SQLException {
                // Wait for delete button to be visible and interact with it
                WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
                WebElement deleteButton = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("delete-btn-1")));
                deleteButton.click();

                // Validate the UI update
                assertTrue(!driver.getPageSource().contains("Updated Task"));

                // Validate in Database
                PreparedStatement checkStmt = conn.prepareStatement("SELECT * FROM todos WHERE title='Updated Task'");
                ResultSet rs = checkStmt.executeQuery();
                assertTrue(!rs.next(), "Task was not deleted from the database.");
            }

            @AfterEach
            public void teardown() throws SQLException {
                if (conn != null && !conn.isClosed()) {
                    conn.close();
                }
                if (driver != null) {
                    driver.quit();
                }
            }
        }