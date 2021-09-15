import { Food } from "./food";

export interface Recommendation {
    foods: Food[];
    majorIngredients: string[];
}