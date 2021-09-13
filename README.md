# Objectives

We will analyze a dataset provided by an e-commerce marketplace called Olist to answer the CEO’s question:

> How to increase customer satisfaction (so as to increase profit margin) while maintaining a healthy order volume?

## About Olist

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers including inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Here are the seller and customer workflows:

**Seller**

- Seller joins Olist
- Seller uploads products catalogue
- Seller gets notified when a product is sold
- Seller hands over an item to the logistic carrier

*Note that multiple sellers can be involved in one customer order!*

**Customer**

- Browses products on the marketplace
- Purchases products from Olist.store
- Gets an expected date for delivery
- Receives the order
- Leaves a review about the order

*A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!*

## Dataset

The dataset consists of 100k orders from 2016 and 2018 that were made on the Olist store, available as a csv on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)

<img src="misc/HRhd2Y0.png" alt="cover" width="800"/>

## Assumptions

**Revenue**

Olist takes a 10% cut on the product price (excl. freight) of each order delivered.
Olist charges 80 BRL by month per seller.

**Review Score Cost**

In the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refunds or unfavorable word of mouth communication. We will assume that we have an estimate measure of the monetary cost for each bad review:

- 1 star:	100 BRL
- 2 stars	50 BRL
- 3 stars	40 BRL
- 4 stars	0 BRL
- 5 stars	0 BRL

In addition, Olist’s IT costs (servers, etc…) increase with the amount of orders processed, albeit less and less rapidly (scale effects).
For the sake of simplicity, we will consider Olist’s total cumulated IT Costs to be proportional to the square-root of the total cumulated number of orders approved. Since the birth of the marketplace, cumulated IT costs have amounted to 500,000 BRL
