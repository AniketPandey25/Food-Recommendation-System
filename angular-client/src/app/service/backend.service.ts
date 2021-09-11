import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Food } from '../model/food';

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private httpClient: HttpClient) { }

  public getRecipe(): Observable<Food[]> {
    return this.httpClient.get<Food[]>("http://localhost:5000/rest/v1/foods");
  }

  public getRecommendation(id: string): Observable<Food[]> {
    return this.httpClient.get<Food[]>("http://localhost:5000/rest/v1/recommendation/" + id);
  }
}
