#!/bin/bash

# Set project name
PROJECT_NAME="todo-automation"
PACKAGE_BASE="com.example"
PACKAGE_PATH="src/main/java/com/example"
TEST_PACKAGE_PATH="src/test/java/com/example"

echo "Creating Maven project: $PROJECT_NAME..."
mvn archetype:generate -DgroupId=$PACKAGE_BASE -DartifactId=$PROJECT_NAME -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

cd $PROJECT_NAME || exit

echo "Setting up project structure..."
mkdir -p src/main/resources
mkdir -p $PACKAGE_PATH/config
mkdir -p $PACKAGE_PATH/utils
mkdir -p src/test/resources
mkdir -p $TEST_PACKAGE_PATH/tests
mkdir -p $TEST_PACKAGE_PATH/pages

# Create pom.xml with required dependencies
cat > pom.xml <<EOL
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>$PACKAGE_BASE</groupId>
    <artifactId>$PROJECT_NAME</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <!-- Selenium -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>4.7.2</version>
        </dependency>
        
        <!-- JUnit -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.8.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.8.1</version>
            <scope>test</scope>
        </dependency>

        <!-- WebDriver Manager -->
        <dependency>
            <groupId>io.github.bonigarcia</groupId>
            <artifactId>webdrivermanager</artifactId>
            <version>5.2.3</version>
        </dependency>

        <!-- MySQL Driver -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.33</version>
        </dependency>
    </dependencies>
</project>
EOL

echo "Creating configuration file..."
cat > src/main/resources/config.properties <<EOL
# Database Configuration
jdbc.url=jdbc:mysql://localhost:3306/todo_db
jdbc.user=root
jdbc.password=password
EOL

echo "Creating Database Utility class..."
cat > $PACKAGE_PATH/utils/DatabaseUtil.java <<EOL
package com.example.utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;
import java.io.InputStream;

public class DatabaseUtil {
    private static String JDBC_URL;
    private static String USER;
    private static String PASSWORD;

    static {
        try (InputStream input = DatabaseUtil.class.getClassLoader().getResourceAsStream("config.properties")) {
            Properties properties = new Properties();
            properties.load(input);
            JDBC_URL = properties.getProperty("jdbc.url");
            USER = properties.getProperty("jdbc.user");
            PASSWORD = properties.getProperty("jdbc.password");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(JDBC_URL, USER, PASSWORD);
    }
}
EOL

echo "Creating Page Object Model for Todo page..."
cat > $TEST_PACKAGE_PATH/pages/TodoPage.java <<EOL
package com.example.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class TodoPage {
    private WebDriver driver;

    public TodoPage(WebDriver driver) {
        this.driver = driver;
    }

    public void addTodoItem(String item) {
        WebElement inputField = driver.findElement(By.id("todo-input"));
        inputField.sendKeys(item);
        WebElement addButton = driver.findElement(By.id("add-btn"));
        addButton.click();
    }

    public boolean isTodoPresent(String item) {
        return driver.getPageSource().contains(item);
    }
}
EOL

echo "Creating Todo Test Class..."
cat > $TEST_PACKAGE_PATH/tests/TodoUITest.java <<EOL
package com.example.tests;

import com.example.utils.DatabaseUtil;
import com.example.pages.TodoPage;
import org.junit.jupiter.api.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TodoUITest {
    private static WebDriver driver;
    private Connection conn;
    private TodoPage todoPage;

    @BeforeAll
    public static void setupClass() {
        WebDriverManager.chromedriver().setup();
    }

    @BeforeEach
    public void setupTest() throws SQLException {
        driver = new ChromeDriver();
        driver.get("http://localhost:8080"); // Update with actual ToDo app URL
        conn = DatabaseUtil.getConnection();
        todoPage = new TodoPage(driver);
    }

    @Test
    public void testAddTodo() throws SQLException {
        todoPage.addTodoItem("Automated Task");

        // Validate in UI
        assertTrue(todoPage.isTodoPresent("Automated Task"));

        // Validate in Database
        PreparedStatement checkStmt = conn.prepareStatement("SELECT * FROM todos WHERE title='Automated Task'");
        ResultSet rs = checkStmt.executeQuery();
        assertTrue(rs.next(), "Task was not added to the database.");
    }

    @Test
    public void testUpdateTodo() throws SQLException {
        // Assuming an update method exists in UI
        driver.findElement(By.id("edit-btn-1")).click();
        WebElement editField = driver.findElement(By.id("edit-input-1"));
        editField.clear();
        editField.sendKeys("Updated Task");
        driver.findElement(By.id("save-btn-1")).click();

        assertTrue(driver.getPageSource().contains("Updated Task"));

        // Validate in Database
        PreparedStatement checkStmt = conn.prepareStatement("SELECT * FROM todos WHERE title='Updated Task'");
        ResultSet rs = checkStmt.executeQuery();
        assertTrue(rs.next(), "Task was not updated in the database.");
    }

    @Test
    public void testDeleteTodo() throws SQLException {
        driver.findElement(By.id("delete-btn-1")).click();
        assertTrue(!driver.getPageSource().contains("Updated Task"));

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
EOL

echo "Setup completed. Navigate to $PROJECT_NAME and run 'mvn test' to execute tests."
