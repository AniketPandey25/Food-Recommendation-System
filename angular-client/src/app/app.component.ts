import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { Food } from './model/food';
import { BackendService } from './service/backend.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  foods: Food[] = [];
  myControl = new FormControl();
  options: Food[] = [];
  filteredOptions: Observable<Food[]> | undefined;
  loading: boolean = false;

  constructor(private backendService: BackendService) { }

  ngOnInit() {
    this.backendService
      .getRecipe()
      .subscribe((recipes) => this.options = recipes);

    this.filteredOptions = this.myControl.valueChanges
      .pipe(
        map(value => {
          return this.options.filter(option => option.name.toLowerCase().includes(value.toLowerCase())).slice(0, 5);
        })
      );
  }

  public onOptionSelected(name: string) {
    const id = this.options.find((option) => option.name == name)?._id.$oid;
    if (id != undefined) {
      this.loading = true;
      this.foods = [];
      this.backendService
        .getRecommendation(id)
        .subscribe(
          (foods) => {
            this.foods = foods;
            this.loading = false;
          }
        );
    }
  }
}
