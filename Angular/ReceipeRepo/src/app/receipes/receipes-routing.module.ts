import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { AuthGuard } from "../auth/auth.guard";
import { ReceipeDetailComponent } from "./receipe-detail/receipe-detail.component";
import { ReceipeEditComponent } from "./receipe-edit/receipe-edit.component";
import { ReceipeResolverService } from "./receipe.resolver";
import { ReceipesComponent } from "./receipes.component";
import { RecipeStartComponent } from "./recipe-start/recipe-start.component";

const routes: Routes = [
  {
    path: "receipes",
    component: ReceipesComponent,
    canActivate: [AuthGuard],
    children: [
      { path: "", component: RecipeStartComponent },
      { path: "new", component: ReceipeEditComponent },
      {
        path: ":id",
        component: ReceipeDetailComponent,
        resolve: [ReceipeResolverService],
      },
      {
        path: ":id/edit",
        component: ReceipeEditComponent,
        resolve: [ReceipeResolverService],
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ReceipesRoutingModule {}
