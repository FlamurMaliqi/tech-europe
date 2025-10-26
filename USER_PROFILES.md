# User Profile System

The drive-thru agent now has access to a vector database with 20 fake user profiles for testing and demonstration purposes.

## Generated User Profiles

The system has generated and stored 20 user profiles with:
- **User IDs**: 1-20
- **Names**: Various realistic names
- **Dietary preferences**: Some profiles have dietary preferences (vegetarian, vegan, gluten-free, keto, dairy-free)
- **Order history**: 3-10 past orders per profile
- **Favorite items**: Based on order history
- **Personal coupons**: Some profiles have active personal coupons
- **Default drinks**: Each profile has a preferred drink

## Sample User IDs

Here are some sample user IDs you can test with:

1. **User ID 1**: Phoenix Thomas (Keto diet)
2. **User ID 2**: Avery Anderson (Vegetarian)
3. **User ID 3**: Riley Taylor (Gluten-free)
4. **User ID 5**: Emery King (No special diet)
5. **User ID 10**: Blake Martinez (No special diet)
6. **User ID 13**: Dakota Johnson (Vegetarian)
7. **User ID 15**: Finley Anderson (No special diet)
8. **User ID 18**: Blake Johnson (Vegetarian)

## How to Test with the Agent

When the drive-thru agent is running, customers can identify themselves by:

1. **Providing their user ID**: "Hi, I'm user 2934" or "My user ID is 2"
2. **Giving their name**: "Hi, I'm Alex" (will search for profiles with that name)

The agent will:
- Look up their profile from the vector database
- Welcome them back by name
- Show their dietary preferences
- Suggest items based on their order history
- Show their available personal coupons
- Remember their favorite items

## Example Conversation

**Agent**: "Welcome to McDonald's! How can I help you today?"

**Customer**: "Hi, my user ID is 2"

**Agent**: "Welcome back, Avery! I found your profile. I see you prefer vegetarian options. You've visited us 5 times. How can I help you today?"

**Customer**: "What are my available coupons?"

**Agent**: [Uses `show_user_coupons` tool to display personal coupons]

**Customer**: "What would you recommend?"

**Agent**: [Uses `get_user_recommendations` tool based on dietary preferences and order history]

## Profile Storage

Profiles are stored in the Kontext vector database at:
```
MCPs/kontext
```
(Relative path from the tech-europe repository root)

Each profile is stored with the key: `user_profile_{user_id}`

## Regenerating Profiles

To regenerate and store new user profiles:

```bash
cd agent
python3 scripts/generate_fake_user_profiles.py
```

## Agent Tools for User Profiles

The agent has the following tools for user profile management:

1. **lookup_user_profile**: Look up a user by ID or name
2. **show_user_coupons**: Display user's personal coupons
3. **get_user_recommendations**: Get personalized recommendations
4. **update_user_preferences**: Update user preferences (dietary, favorites, etc.)

## Profile Data Structure

Each user profile contains:

```json
{
  "user_id": "2",
  "name": "Avery Anderson",
  "email": "avery.anderson@example.com",
  "phone": "+1-555-123-4567",
  "member_since": "2025-05-06T12:04:04.985406",
  "visit_count": 5,
  "preferences": {
    "dietary": ["vegetarian"],
    "favorite_items": ["Big Mac", "Fries", "Salad"],
    "default_drink": "Coca-Cola",
    "avoid_items": [],
    "spice_level": "medium",
    "size_preference": "medium"
  },
  "order_history": [
    {
      "order_id": "ORD-2-001",
      "date": "2025-06-23T12:04:04.985359",
      "items": ["Quarter Pounder", "McDouble", "Fries"],
      "total_amount": 20.94,
      "status": "completed"
    }
  ],
  "coupons": [
    {
      "name": "Free Medium Fries",
      "code": "FREEFRIES2",
      "type": "free_item",
      "item": "Fries",
      "status": "active",
      "expiration": "2025-12-31T00:00:00",
      "description": "Valid until 2025-12-31"
    }
  ]
}
```

## Notes

- The agent is already configured to use these profiles
- Profiles are stored in a Kontext vector database for fast retrieval
- The agent can search by name or user ID
- Profiles include realistic order histories, dietary preferences, and coupons
- Each profile has been visited 3-10 times with corresponding order history

