Capstone Project Part 1: Event Ticket Marketplace  
Project Idea: Event Ticket Marketplace App 
A web application where users can sell tickets for their events and **buy tickets** for events they want to attend.  
The app allows sellers to create events, set ticket prices, and track sales, while buyers can browse, filter, and purchase tickets for events. 

 Main Features
Seller Features:
Create an event with title, description, location, date, time, ticket price, and quantity.  
View list of sold tickets.  
Edit or delete events.  

Buyer Features: 
Browse all upcoming events.  
Search and filter events by category, location, or date.  
Purchase tickets (mock payment).  
View purchased tickets.  

Optional Features:
- Generate QR codes for purchased tickets.  
- Send email confirmation for ticket purchase.  
- Event categories (music, sports, workshop, etc.).  


APIs
Geolocation API → Show events near the user’s location.  
Payment API (sandbox) → Mock payments using Stripe or similar.  


Django Apps & Endpoints  
Apps:  
1. Users  → Manage authentication and user profiles.  
2. Events  → Manage event creation and listings.  
3. Tickets  → Handle ticket purchases and tracking.  
Endpoints:
Events → List all events (GET)  
Events create → Create new event (POST)  
Events → Retrieve, update, or delete event (GET, PUT, DELETE)  
Tickets purchase → Buy a ticket (POST)  
Tickets my-tickets → View purchased tickets (GET)  


Database Schema
User Model: 
Username: CharField  
Email: EmailField  
Password: CharField  
Role: CharField (buyer/seller/both)  

Event Model: 
Title : CharField  
Description : TextField  
Location : CharField  
Date : DateField  
Time : TimeField  
Price : DecimalField  
Total tickets : IntegerField  
Seller : ForeignKey to `User  

Ticket Model:  
Event : ForeignKey to `Event`  
Buyer : ForeignKey to `User`  
Purchase_date : DateTimeField  
Ticket_code : CharField (optional, for QR code)  

Relationships:
One seller → Many events  
One event → Many tickets  
One buyer → Many tickets  
