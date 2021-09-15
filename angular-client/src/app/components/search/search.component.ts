import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable, Subject } from 'rxjs';
import { map } from 'rxjs/operators'
import { Food } from 'src/app/models/food';
import { BackendService } from 'src/app/services/backend/backend.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {
  foodRecipe: Food[] = [];
  parentSubject: Subject<any> = new Subject();
  filteredFoodRecipe: Observable<Food[]> | undefined;
  cookTimeFormControl: FormControl = new FormControl();
  searchBoxFormControl: FormControl = new FormControl();

  constructor(private backendService: BackendService) { }

  ngOnInit(): void {
    /**
     * Get all the food recipe
     * and store in memory
     */
    this.backendService.getAllFoodRecipe().subscribe((data) => this.foodRecipe = data);

    /**
     * Filter on the basis of value provided
     * in the search box
     */
    this.filteredFoodRecipe = this.searchBoxFormControl.valueChanges.pipe(
      map((value) => this.foodRecipe.filter((option) => option.name.toLowerCase().includes(value.toLowerCase())).slice(0, 5))
    );
  }

  public onOptionSelected(event: any): void {
    const cookTime = this.cookTimeFormControl.value;
    const selectedRecipeId = this.foodRecipe.find((recipe) => recipe.name == this.searchBoxFormControl.value)?._id.$oid;
    this.parentSubject.next({
      'cookTime': cookTime,
      'selectedRecipeId': selectedRecipeId
    });
  }

}
