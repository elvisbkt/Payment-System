import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {
    Router
  } from '@angular/router';
import {
Observable
} from 'rxjs';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

    private apiRoot = 'http://127.0.0.1:8000/api/';
    constructor(private http: HttpClient, private router: Router) { }

    getUserById(userId): Observable < any > {
        return this.http.get(this.apiRoot.concat('user/') + userId + '/');
    }
    createNewHospital(hospital): Observable < any > {
    return this.http.post(this.apiRoot.concat('hospital/'), hospital);
    }

    getAllhospitals(): Observable < any > {
    return this.http.get(this.apiRoot.concat('hospital/'));
    }
}
