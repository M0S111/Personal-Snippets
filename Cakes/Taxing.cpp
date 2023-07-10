#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

class TaxPayer{
	
protected:
	
	string TaxPayerName;
	double PropertyValue;
	bool Filer;
	
public:


	TaxPayer(string PyN = "",bool F = true,double pv=0)
	:TaxPayerName(PyN),PropertyValue(pv),Filer(F)
	{
	}
	
	double GetPropertyValue()
	{
		return PropertyValue;
	}
	
	double GetAdvanceIncomeTax()
	{
		double tx;
		
		if (Filer)
		{
			tx = 0.02 * PropertyValue;
		}
		else
		{
			tx = 0.04 * PropertyValue;
		}
		
		return tx;
	}
	
	virtual void TotalTax()
	{
		GetAdvanceIncomeTax();	
	}		
};

class Seller: public TaxPayer
{
	double PropertyPurchaseValue;
	int SaleYear;
	
public:
	
	Seller(string Name,bool File,double propval,double purchval,int syear)
	:PropertyPurchaseValue(purchval),SaleYear(syear)
	{
		TaxPayerName = Name;
		PropertyValue = propval;
		Filer = File;
	}
	
	double CalcCGT()
	{
		double profit;
		double tx;
		
		profit = PropertyValue - PropertyPurchaseValue;
		
		if (profit > 0 && SaleYear <= 1)
		{
			tx = profit * 0.1;
		}
		if (profit > 0 && SaleYear == 2)
		{
			tx = profit * 0.075;
		}
		if (profit > 0 && SaleYear > 2)
		{
			tx = profit * 0.05;
		}
		if (profit < 0)
		{
			tx = NULL;
		}
		
		return tx;
	}
	
	void TotalTax()
	{
		double tottax;
		double val;
		double adTax;
		double CGT;
		
		tottax = GetAdvanceIncomeTax() + CalcCGT();
		
		adTax = GetAdvanceIncomeTax();
		val = GetPropertyValue();
		CGT = CalcCGT();
		
		cout << endl;
		cout << "\nSeller: " << TaxPayerName;
		cout << "\nProperty Value: " << val;
		cout << "\nAdvance Income Tax: " << adTax;
		cout << "\nCapital Gains Tax: " << CGT;
		cout << "\nTotal Tax: " << tottax ;
		
	}
};

class Purchaser: public TaxPayer
{
	
	double StampDuty;
	double CapitalValueTax;
	

public:
	
	Purchaser(string Name,bool File,double propval)
	{
		TaxPayerName = Name;
		PropertyValue = propval;
		Filer = File;
		StampDuty = PropertyValue * 0.02;
		CapitalValueTax = PropertyValue * 0.03;
	}
	
	void TotalTax()
	{
		double tottax;
		double val;
		double adTax;
		
		tottax = GetAdvanceIncomeTax() + StampDuty + CapitalValueTax;
		val = GetPropertyValue();
		adTax = GetAdvanceIncomeTax();
		
		cout << endl;
		cout << "\nPurchaser: " << TaxPayerName;
		cout << "\nProperty Value: " << val;
		cout << "\nAdvance Income Tax: " << adTax;
		cout << "\nStamp Duty: " << StampDuty;
		cout << "\nCapital Value Tax: "<< CapitalValueTax;
		cout << "\nTotal Tax: " << tottax ;	
	}
	
	
	
};

int main()
{
	Seller TP("John",true,750000,550000,1);
	
	TP.TotalTax();
	
	Purchaser TP2("Alice",false,445000);
	
	TP2.TotalTax();	
}