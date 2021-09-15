export interface Food {
    _id: {
        $oid: string;
    };
    name: string;
    cookTime: number;
    cuisine: string;
    recipe: string[];
    ingredients: string[];
    image: string;
}