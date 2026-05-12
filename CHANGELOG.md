# Changelog

All notable changes to this project are documented in this file.

## [Unreleased] - 2026-05-12

### Added
- `POST /api/users/login` endpoint for logging in existing users.
- Client-side session persistence using `localStorage` (`chatappUser`).
- Logout button to clear session and close WebSocket connection.
- Smart auth form: tries login first, registers automatically if user doesn't exist.
- Client-side filtering of incoming WebSocket messages to show only messages for the active conversation.

### Fixed
- Message ordering issue in chat history: messages are now sorted oldest → newest when loading a conversation.
- Prevented interleaving of messages from other conversations in the current chat view.

### Notes
- No database schema changes were required; all changes are additive and backward-compatible.
