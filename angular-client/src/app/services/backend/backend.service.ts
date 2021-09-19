import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Food } from 'src/app/models/food';
import { Recommendation } from 'src/app/models/recommendation';

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private httpClient: HttpClient) { }

  /**
   * GET all food recipe 
   * @returns Observable
   */
  public getAllFoodRecipe(): Observable<Food[]> {
    return this.httpClient.get<Food[]>("http://localhost:5000/rest/v1/foods");
  }

  /**
   * GET recommended food recipe 
   * @param id Selected recipe id
   */
  public getRecommendation(id: string): Observable<Recommendation> {
    return this.httpClient.get<Recommendation>("http://localhost:5000/rest/v1/recommendation/" + id);
  }

  /**
   * GET recommended food recipe which can be prepared
   * in cook time 
   * @param id Selected recipe id
   * @param cookTime Cook time
   */
  public getRecommendationWithCookTime(id: string, cookTime: string): Observable<Recommendation> {
    return this.httpClient.get<Recommendation>("http://localhost:5000/rest/v1/recommendation/" + id, {
      params: new HttpParams().set('cookTime', cookTime)
    });
  }

  /**
   * 
   * @param formData 
   * @returns 
   */
  public uploadImage(formData: FormData): Observable<Food[]> {
    return this.httpClient.post<Food[]>("http://localhost:5000/rest/v1/upload", formData);
  }
}
