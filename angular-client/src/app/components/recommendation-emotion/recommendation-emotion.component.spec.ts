import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecommendationEmotionComponent } from './recommendation-emotion.component';

describe('RecommendationEmotionComponent', () => {
  let component: RecommendationEmotionComponent;
  let fixture: ComponentFixture<RecommendationEmotionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RecommendationEmotionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RecommendationEmotionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
