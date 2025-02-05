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
