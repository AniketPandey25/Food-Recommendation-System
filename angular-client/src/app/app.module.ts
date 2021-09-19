import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { HttpClientModule } from '@angular/common/http';
import { MatInputModule } from '@angular/material/input';
import { BrowserModule } from '@angular/platform-browser';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { SearchComponent } from './components/search/search.component';
import { BackendService } from 'src/app/services/backend/backend.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RecommendationComponent } from './components/recommendation/recommendation.component';
import { SelectedRecipeComponent } from './components/selected-recipe/selected-recipe.component';
import { RecommendationEmotionComponent } from './components/recommendation-emotion/recommendation-emotion.component';



@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    SelectedRecipeComponent,
    RecommendationComponent,
    RecommendationEmotionComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    MatCardModule,
    MatIconModule,
    MatListModule,
    MatInputModule,
    MatSelectModule,
    MatButtonModule,
    HttpClientModule,
    MatToolbarModule,
    MatGridListModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    MatAutocompleteModule,
    BrowserAnimationsModule
  ],
  providers: [BackendService],
  bootstrap: [AppComponent]
})
export class AppModule { }
