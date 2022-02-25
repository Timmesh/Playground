import { Component, OnDestroy, OnInit } from "@angular/core";
import { Subscription } from "rxjs";
import { LoggingService } from "../logging.service";
import { Ingredient } from "../shared/ingredients.model";
import { ShoppingListService } from "./shopping-List.service";

@Component({
  selector: "app-shopping-list",
  templateUrl: "./shopping-list.component.html",
  styleUrls: ["./shopping-list.component.css"],
})
export class ShoppingListComponent implements OnInit, OnDestroy {
  ingredients: Ingredient[];
  ingredientSubscription: Subscription;

  constructor(private shoppingListService: ShoppingListService, private loggingService: LoggingService) {}

  ngOnInit() {
    this.ingredients = this.shoppingListService.getIngredients();
    this.ingredientSubscription =
      this.shoppingListService.ingredientsUpdated.subscribe(
        (ingredients) => (this.ingredients = ingredients)
      );
      this.loggingService.printLog("Hello From ShoppingListComponent");

  }

  editItem(index: number) {
    this.shoppingListService.ingredientEdited.next(index);
  }

  ngOnDestroy(): void {
    this.ingredientSubscription.unsubscribe();
  }
}
