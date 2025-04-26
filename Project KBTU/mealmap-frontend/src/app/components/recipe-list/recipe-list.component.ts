import { Component, OnInit } from '@angular/core';
import { RecipeService } from '../../services/recipe.service';

@Component({ selector: 'app-recipe-list', template: `
<div *ngIf="recipes; else loading">
  <h2>Recipes</h2>
  <ul>
    <li *ngFor="let r of recipes">{{ r.title }} ({{ r.calories }} kcal)</li>
  </ul>
  <button (click)="loadRecipes()">Reload</button>
</div>
<ng-template #loading>Loading...</ng-template>
` })
export class RecipeListComponent implements OnInit {
  recipes: any[] = [];
  constructor(private svc: RecipeService) {}
  ngOnInit() { this.loadRecipes(); }
  loadRecipes() { this.svc.getRecipes().subscribe(data => this.recipes = data); }
}