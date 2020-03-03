import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { tap, shareReplay } from 'rxjs/operators';

import * as jwtDecode from 'jwt-decode';
import * as moment from 'moment';
@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

    constructor(private http: HttpClient) { }

    private apiRoot = 'http://127.0.0.1:8000/api/';

    private setSession(authResult) {
        const token = authResult.token;
        const payload = jwtDecode(token);
        const expiresAt = moment.unix(payload.exp);

        localStorage.setItem('token', authResult.token);
        localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
    }
    login(email: string, password: string) {
        return this.http.post(this.apiRoot.concat('auth/login/'), {email, password}).pipe(
            tap(response => this.setSession(response)), shareReplay(),
            );
        }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
    }

    signup(username: string, email: string, password: string) {
        return this.http.post(
          this.apiRoot.concat('auth/register/'),
          { username, email, password}
        );
      }

}
