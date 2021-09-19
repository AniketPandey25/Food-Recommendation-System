import { Component, Input, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { Food } from 'src/app/models/food';
import { BackendService } from 'src/app/services/backend/backend.service';

@Component({
  selector: 'app-recommendation-emotion',
  templateUrl: './recommendation-emotion.component.html',
  styleUrls: ['./recommendation-emotion.component.scss']
})
export class RecommendationEmotionComponent implements OnInit {

  foods!: Food[];
  selectedFood: Food | undefined;
  @Input('recommendationEmotionSubject') recommendationEmotionSubject!: Subject<any>


  constructor(private backendService: BackendService) { }

  ngOnInit(): void {
    this.recommendationEmotionSubject.subscribe((data) => {
      const formData = new FormData();
      formData.append("file", data);
      this.backendService.uploadImage(formData).subscribe((foods) => this.foods = foods);
    });
  }

  public onFoodSelect(food: Food): void {
    this.selectedFood = food;
  }

}
