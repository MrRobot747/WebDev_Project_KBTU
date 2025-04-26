import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private base = 'http://localhost:8000/api/auth';
  constructor(private http: HttpClient) {}
  login(username: string, password: string) {
    return this.http.post<any>(`${this.base}/login/`, { username, password })
      .pipe(tap(res => localStorage.setItem('access_token', res.access)));
  }
  logout() { localStorage.removeItem('access_token'); }
  isLoggedIn(): boolean { return !!localStorage.getItem('access_token'); }
}