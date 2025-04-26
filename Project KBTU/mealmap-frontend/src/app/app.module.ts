import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { JwtModule } from '@auth0/angular-jwt';
import { FormsModule } from '@angular/forms';
import { JwtInterceptor } from './interceptors/jwt.interceptor';
import { LoginComponent } from './components/login/login.component';
import { RecipeListComponent } from './recipe-list/recipe-list.component';


export function tokenGetter() {
  return localStorage.getItem('access_token');
}

@NgModule({
  declarations: [AppComponent, LoginComponent, RecipeListComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    JwtModule.forRoot({ config: { tokenGetter, allowedDomains: ['localhost:8000'] } })
  ],
  providers: [{ provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true }],
  bootstrap: [AppComponent]
})
export class AppModule { }