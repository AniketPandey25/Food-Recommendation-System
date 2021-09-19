import { Component, Input, OnInit } from '@angular/core';
import { Food } from 'src/app/models/food';

@Component({
  selector: 'app-selected-recipe',
  templateUrl: './selected-recipe.component.html',
  styleUrls: ['./selected-recipe.component.scss']
})
export class SelectedRecipeComponent implements OnInit {

  @Input('selectedFood') selectedFood: Food | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
