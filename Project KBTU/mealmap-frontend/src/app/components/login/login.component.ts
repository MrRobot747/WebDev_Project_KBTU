import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({ selector: 'app-login', template: `
<form (ngSubmit)="onSubmit()">
  <input name="username" [(ngModel)]="username" placeholder="Username" />
  <input name="password" type="password" [(ngModel)]="password" placeholder="Password" />
  <button type="submit">Login</button>
</form>
` })
export class LoginComponent {
  username = '';
  password = '';
  constructor(private auth: AuthService, private router: Router) {}
  onSubmit() {
    this.auth.login(this.username, this.password).subscribe(() => this.router.navigate(['/recipes']));
  }
}