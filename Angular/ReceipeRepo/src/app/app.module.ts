import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";
import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { BrowserModule } from "@angular/platform-browser";
import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { AuthInterceptorService } from "./auth/auth-interceptor-service";
import { AuthComponent } from "./auth/auth.component";
import { CoreModule } from "./core.module";
import { HeaderComponent } from "./header/header.component";
import { ReceipeService } from "./receipes/receipe.service";
import { ReceipesModule } from "./receipes/receipes.module";
import { DropdownDirective } from "./shared/dropdown.directive";
import { SharedModule } from "./shared/shared.module";
import { ShoppingListModule } from "./shopping-list/shopping-list.module";
import { ShoppingListService } from "./shopping-list/shopping-List.service";

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    AuthComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
    ReceipesModule,
    ShoppingListModule,
    SharedModule,
    CoreModule
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
