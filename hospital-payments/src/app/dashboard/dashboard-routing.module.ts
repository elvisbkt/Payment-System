import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from './dashboard.component';
import { PaymentPageComponent } from './payment-page/payment-page.component';
import { ReportsPageComponent } from './reports-page/reports-page.component';
import { UserPaymentPageComponent } from './user-payment-page/user-payment-page.component';

const DASHBOARD_ROUTES: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
    children: [
      {
        path: 'payments',
        component: PaymentPageComponent
      },
      {
        path: 'reports',
        component: ReportsPageComponent
      },
      {
        path: 'user-payments',
        component: UserPaymentPageComponent
      },
      {
        path: '',
        pathMatch: 'full',
        redirectTo: 'user-payments'
      }]
  }];
@NgModule({
  imports: [RouterModule.forChild(DASHBOARD_ROUTES)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
