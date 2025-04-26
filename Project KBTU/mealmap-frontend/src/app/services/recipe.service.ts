import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class RecipeService {
  private base = 'http://localhost:8000/api/recipes';
  constructor(private http: HttpClient) {}
  getRecipes(): Observable<any[]> { return this.http.get<any[]>(this.base + '/'); }
  createRecipe(data: any) { return this.http.post(this.base + '/', data); }
}