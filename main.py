//+------------------------------------------------------------------+
//|                                                BB test strat.mq4 |
//|                        Copyright 2021, MetaQuotes Software Corp. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2021, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property strict
#include <customfunction01.mqh>



int bbPeriod = 20;
int band1Std = 1;
int band2Std = 4;
input double riskPerTrade = 0.02;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//---
   Alert("");
   Alert("The EA just started.");
   
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//---
   Alert("The EA just closed.");
   
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//---

   Alert("");
   
   Alert(MarketInfo(NULL,MODE_STOPLEVEL));
   
   
   
   
   double bbLower1 = iBands(NULL,0,bbPeriod,band1Std,0,PRICE_CLOSE,MODE_LOWER,0);
   double bbUpper1 = iBands(NULL,0,bbPeriod,band1Std,0,PRICE_CLOSE,MODE_UPPER,0);
   double bbMid = iBands(NULL,0,bbPeriod,band1Std,0,PRICE_CLOSE,0,0);
   
   double bbLower2 = iBands(NULL,0,bbPeriod,band2Std,0,PRICE_CLOSE,MODE_LOWER,0);
   double bbUpper2 = iBands(NULL,0,bbPeriod,band2Std,0,PRICE_CLOSE,MODE_UPPER,0);
   
   if(Ask < bbLower1)//buying
   {
      Alert("Price is bellow bbLower1, Sending buy order");
      double stopLossPrice = NormalizeDouble(bbLower2,Digits);
      double takeProfitPrice = NormalizeDouble(bbMid,Digits);;
      Alert("Entry Price = " + Ask);
      Alert("Stop Loss Price = " + stopLossPrice);
      Alert("Take Profit Price = " + takeProfitPrice);
      
      double lotSize = optimalLotSize(riskPerTrade,Ask,stopLossPrice);
      
      int orderID = OrderSend(NULL,OP_BUYLIMIT,0.01,Ask,10,stopLossPrice,takeProfitPrice);
      if(orderID < 0) Alert("order rejected. Order error: " + GetLastError());
   }
   else if(Bid > bbUpper1)//shorting
   {
      Alert("Price is above bbUpper1, Sending short order");
      double stopLossPrice = NormalizeDouble(bbUpper2,Digits);
      double takeProfitPrice = NormalizeDouble(bbMid,Digits);
      Alert("Entry Price = " + Bid);
      Alert("Stop Loss Price = " + stopLossPrice);
      Alert("Take Profit Price = " + takeProfitPrice);
      
      double lotSize = optimalLotSize(riskPerTrade,Bid,stopLossPrice);
	  
	  int orderID = OrderSend(NULL,OP_SELLLIMIT,0.01,Bid,10,stopLossPrice,takeProfitPrice);
	  if(orderID < 0) Alert("order rejected. Order error: " + GetLastError());
   }
   
  }
//+------------------------------------------------------------------+
