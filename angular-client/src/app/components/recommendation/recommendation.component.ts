import { from, Observable, of, Subject } from 'rxjs';
import { Component, Input, OnInit } from '@angular/core';
import { Recommendation } from 'src/app/models/recommendation';
import { BackendService } from 'src/app/services/backend/backend.service';
import { FormControl } from '@angular/forms';
import { Food } from 'src/app/models/food';


@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.scss']
})
export class RecommendationComponent implements OnInit {
  selectedFood: Food | undefined;
  recommendation!: Recommendation;
  checkBoxFormControl = new FormControl();
  filteredRecommendation!: Observable<Food[]>;
  selectedIngredients: string[] = new Array();
  @Input('parentSubject') parentSubject!: Subject<any>;

  constructor(private backendService: BackendService) { }

  ngOnInit(): void {
    this.parentSubject.subscribe(event => {
      const cookTime = event.cookTime;
      const selectedRecipeId = event.selectedRecipeId;

      /**
       * 
       */
      if (cookTime != null) {
        this.backendService
          .getRecommendationWithCookTime(selectedRecipeId, cookTime)
          .subscribe(data => {
            this.recommendation = data;
            this.filteredRecommendation = of(this.recommendation.foods);
          });
      } else {
        this.backendService
          .getRecommendation(selectedRecipeId)
          .subscribe(data => {
            this.recommendation = data;
            this.filteredRecommendation = of(this.recommendation.foods);
          });
      }
    });
  }

  ngOnngOnDestroy(): void {
    this.parentSubject.unsubscribe();
  }

  public onSelectionChange(event: any): void {
    const ingredient = event.options[0].value;
    const selected = event.options[0].selected;

    /**
     * Remove ingredients according to selection 
     */
    if (selected) {
      this.selectedIngredients.push(ingredient);
    } else {
      this.selectedIngredients.splice(this.selectedIngredients.indexOf(ingredient), 1);
    }

    /**
     * 
     */
    if (this.selectedIngredients.length == 0) {
      this.filteredRecommendation = of(this.recommendation.foods);
    } else {
      this.filteredRecommendation = of(this.recommendation.foods.filter(
        (food) => this.selectedIngredients.every((ingredient) => food.ingredients.includes(ingredient))
      ));
    }
    console.log(this.selectedIngredients);
  }

  public onFoodSelect(food: Food): void {
    this.selectedFood = food;
  }
}
