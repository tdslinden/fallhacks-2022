import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { HistoryComponent } from './history/history.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavBarComponent } from './main/nav-bar/nav-bar.component';
const appRoute: Routes = [
  { path: '', component: MainComponent },
  { path: 'hist', component:HistoryComponent}
] 
@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    HistoryComponent,
    NavBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    RouterModule.forRoot(appRoute)
  ],
  providers: [],
  bootstrap: [AppComponent, MainComponent,NavBarComponent]
})
export class AppModule { }
