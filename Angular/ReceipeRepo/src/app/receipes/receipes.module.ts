import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { ReactiveFormsModule } from "@angular/forms";
import { RouterModule } from "@angular/router";
import { ReceipeDetailComponent } from "./receipe-detail/receipe-detail.component";
import { ReceipeEditComponent } from "./receipe-edit/receipe-edit.component";
import { ReceipeItemComponent } from "./receipe-list/receipe-item/receipe-item.component";
import { ReceipeListComponent } from "./receipe-list/receipe-list.component";
import { ReceipesRoutingModule } from "./receipes-routing.module";
import { ReceipesComponent } from "./receipes.component";
import { RecipeStartComponent } from "./recipe-start/recipe-start.component";

@NgModule({
  declarations: [
    ReceipesComponent,
    ReceipeListComponent,
    ReceipeDetailComponent,
    ReceipeItemComponent,
    RecipeStartComponent,
    ReceipeEditComponent,
  ],
  imports: [
    RouterModule,
    CommonModule,
    ReactiveFormsModule,
    ReceipesRoutingModule,
  ],
  exports: [
    ReceipesComponent,
    ReceipeListComponent,
    ReceipeDetailComponent,
    ReceipeItemComponent,
    RecipeStartComponent,
    ReceipeEditComponent,
  ],
})
export class ReceipesModule {}
