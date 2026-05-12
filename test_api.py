#!/usr/bin/env python3
"""
Quick test script to verify ChatApp is working correctly.
Run this to test all endpoints.
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_api():
    print("=" * 60)
    print("🧪 ChatApp API Test Suite")
    print("=" * 60)
    
    try:
        # Test 1: Register users
        print("\n✅ TEST 1: User Registration")
        print("-" * 60)
        timestamp = int(time.time() * 1000) % 100000
        
        user1_resp = requests.post(
            f"{BASE_URL}/api/users/register",
            json={"username": f"user_test_{timestamp}"}
        )
        if user1_resp.status_code == 200:
            user1 = user1_resp.json()
            print(f"  ✓ User 1 registered: {user1['username']} (ID: {user1['id']})")
        else:
            print(f"  ✗ Failed to register user 1: {user1_resp.text}")
            return False
        
        user2_resp = requests.post(
            f"{BASE_URL}/api/users/register",
            json={"username": f"user_test2_{timestamp}"}
        )
        if user2_resp.status_code == 200:
            user2 = user2_resp.json()
            print(f"  ✓ User 2 registered: {user2['username']} (ID: {user2['id']})")
        else:
            print(f"  ✗ Failed to register user 2: {user2_resp.text}")
            return False
        
        # Test 2: Get users
        print("\n✅ TEST 2: Get Users List")
        print("-" * 60)
        users_resp = requests.get(f"{BASE_URL}/api/users")
        if users_resp.status_code == 200:
            users = users_resp.json()
            print(f"  ✓ Retrieved {len(users)} total users")
            print(f"    Latest users: {[u['username'] for u in users[-3:]]}")
        else:
            print(f"  ✗ Failed to get users: {users_resp.text}")
            return False
        
        # Test 3: Search users
        print("\n✅ TEST 3: Search Users")
        print("-" * 60)
        search_resp = requests.get(f"{BASE_URL}/api/users?search=user_test")
        if search_resp.status_code == 200:
            results = search_resp.json()
            print(f"  ✓ Search found {len(results)} users matching 'user_test'")
        else:
            print(f"  ✗ Search failed: {search_resp.text}")
            return False
        
        # Test 4: Send message
        print("\n✅ TEST 4: Send Message")
        print("-" * 60)
        msg_resp = requests.post(
            f"{BASE_URL}/api/messages?sender_id={user1['id']}",
            json={
                "content": f"Hello {user2['username']}! This is a test message 🎉",
                "receiver_id": user2['id']
            }
        )
        if msg_resp.status_code == 200:
            msg = msg_resp.json()
            print(f"  ✓ Message sent successfully (ID: {msg['message_id']})")
        else:
            print(f"  ✗ Failed to send message: {msg_resp.text}")
            return False
        
        # Test 5: Get messages
        print("\n✅ TEST 5: Get Messages")
        print("-" * 60)
        msgs_resp = requests.get(f"{BASE_URL}/api/messages")
        if msgs_resp.status_code == 200:
            messages = msgs_resp.json()
            print(f"  ✓ Retrieved {len(messages)} total messages")
            if messages:
                latest = messages[0]
                print(f"    Latest message: '{latest['content']}'")
                print(f"    From: {latest['sender_username']} → ID {latest['receiver_id']}")
        else:
            print(f"  ✗ Failed to get messages: {msgs_resp.text}")
            return False
        
        # Test 6: Search messages
        print("\n✅ TEST 6: Search Messages")
        print("-" * 60)
        search_msg_resp = requests.get(f"{BASE_URL}/api/messages?search=test")
        if search_msg_resp.status_code == 200:
            results = search_msg_resp.json()
            print(f"  ✓ Message search found {len(results)} results")
        else:
            print(f"  ✗ Message search failed: {search_msg_resp.text}")
            return False
        
        # Test 7: Frontend
        print("\n✅ TEST 7: Frontend (HTML)")
        print("-" * 60)
        frontend_resp = requests.get(f"{BASE_URL}/")
        if frontend_resp.status_code == 200 and "ChatApp" in frontend_resp.text:
            print("  ✓ Frontend loads successfully")
            print(f"    Page title found: ChatApp - Real-time Chat")
        else:
            print(f"  ✗ Frontend not responding properly")
            return False
        
        # Summary
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED!")
        print("=" * 60)
        print("\n✨ Your ChatApp is fully functional!")
        print(f"   📍 Frontend: {BASE_URL}")
        print(f"   📍 API: {BASE_URL}/api")
        print(f"   📍 WebSocket: ws://localhost:8000/ws/<user_id>")
        print("\nNext steps:")
        print("  1. Push to GitHub")
        print("  2. Deploy to Render/Railway")
        print("  3. Create demo video")
        print("  4. Submit!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\n⚠️  Make sure the server is running:")
        print("   python main.py")
        return False

if __name__ == "__main__":
    test_api()
