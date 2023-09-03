import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  constructor(private http: HttpClient) {}

  // Define your API base URL here
  private apiUrl = 'http://your-flask-api-url/';

  // Add methods to interact with your Flask API
}
