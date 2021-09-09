import { Component, OnInit } from '@angular/core';
import { Food } from './model/food';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  foods: Food[] = [
    {
      id: "",
      name: "Masala Karela Recipe",
      cookTime: 45,
      cuisine: "Indian",
      recipe: [],
      ingredients: [],
      image: "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/Pooja_Thakur/Karela_Masala_Recipe-4_1600.jpg"
    },
    {
      id: "",
      name: "Masala Karela Recipe",
      cookTime: 45,
      cuisine: "Indian",
      recipe: [],
      ingredients: [],
      image: "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/Pooja_Thakur/Karela_Masala_Recipe-4_1600.jpg"
    },
    {
      id: "",
      name: "Masala Karela Recipe",
      cookTime: 45,
      cuisine: "Indian",
      recipe: [],
      ingredients: [],
      image: "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/Pooja_Thakur/Karela_Masala_Recipe-4_1600.jpg"
    },
    {
      id: "",
      name: "Masala Karela Recipe",
      cookTime: 45,
      cuisine: "Indian",
      recipe: [],
      ingredients: [],
      image: "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/Pooja_Thakur/Karela_Masala_Recipe-4_1600.jpg"
    }
  ];
}
