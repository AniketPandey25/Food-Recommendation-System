import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectedRecipeComponent } from './selected-recipe.component';

describe('SelectedRecipeComponent', () => {
  let component: SelectedRecipeComponent;
  let fixture: ComponentFixture<SelectedRecipeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectedRecipeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectedRecipeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
