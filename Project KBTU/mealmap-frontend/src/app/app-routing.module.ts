import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RecipeListComponent } from './components/recipe-list/recipe-list.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'recipes', component: RecipeListComponent },
  { path: '', redirectTo: 'recipes', pathMatch: 'full' }
];

@NgModule({ imports: [RouterModule.forRoot(routes)], exports: [RouterModule] })
export class AppRoutingModule { }

