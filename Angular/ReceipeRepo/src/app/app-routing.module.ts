import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { AuthComponent } from "./auth/auth.component";
import { ShoppingListComponent } from "./shopping-list/shopping-list.component";

const appRoutes: Routes = [
  { path: "", redirectTo: "receipes", pathMatch: "full" },
  /* Older Version
  {
    path: "receipes",
    loadChildren: "./receipes/receipes.module#ReceipesModule",
  }, */
  {
    path: "receipes",
    loadChildren: () =>
      import("./receipes/receipes.module").then((m) => m.ReceipesModule),
  },
];
@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
