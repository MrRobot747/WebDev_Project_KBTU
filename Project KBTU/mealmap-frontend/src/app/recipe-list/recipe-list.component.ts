import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

// Определим интерфейс для рецепта
interface Recipe {
  id: number;
  name: string;
  description: string;
  // Добавь другие поля, которые тебе нужны
}

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipes: Recipe[] = [];  // Теперь это массив объектов типа Recipe

  constructor(private http: HttpClient) {}

  ngOnInit() {
    // Получаем данные с API
    this.http.get<Recipe[]>(`${environment.apiUrl}/recipes/`)
      .subscribe(data => {
        this.recipes = data;  // Тип данных теперь правильно привязан
      });
  }
}
