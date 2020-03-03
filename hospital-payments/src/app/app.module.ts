import { DashboardRoutingModule } from './dashboard/dashboard-routing.module';
import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { MatNativeDateModule } from '@angular/material';


import {ErrorInterceptor} from './interceptors/error.interceptor';
import {JwtInterceptor} from './interceptors/jwt.interceptor';

import {appRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import {AlertComponent} from './directives/alert/alert.component';
import {HomeComponent} from './home/home.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { DashboardModule } from './dashboard/dashboard.module';

@NgModule({
    declarations: [
        AppComponent, LoginComponent, RegisterComponent, AlertComponent, HomeComponent, DashboardComponent
    ],
    imports: [
        BrowserModule, ReactiveFormsModule,
        HttpClientModule,
        appRoutingModule,
        BrowserAnimationsModule,
        FormsModule,
        DashboardModule,
        DashboardRoutingModule
    ],
    entryComponents: [AppComponent],
    providers: [
      { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
      { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },
    ],
    bootstrap: [AppComponent]
})
export class AppModule {}
