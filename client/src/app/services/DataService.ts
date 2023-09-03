import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  constructor(private http: HttpClient) {}

  private apiUrl = 'http://your-flask-api-url/';

  createTables(): Observable<any> {
    return this.http.get(this.apiUrl + 'create_tables');
  }

  getUsers(): Observable<any> {
    return this.http.get(this.apiUrl + 'get_users');
  }

  getIncomeSources(): Observable<any> {
    return this.http.get(this.apiUrl + 'get_income_sources');
  }

  getExpenses(): Observable<any> {
    return this.http.get(this.apiUrl + 'get_expenses');
  }

  getSavingsGoals(): Observable<any> {
    return this.http.get(this.apiUrl + 'get_savings_goals');
  }

  createFakeUsers(numUsers: number): Observable<any> {
    return this.http.post(this.apiUrl + `create_fake_users/${numUsers}`, {});
  }
}
