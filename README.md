
[![main pipeline](https://github.com/Aliyas-22/github-actions-capstone/actions/workflows/main-pipeline.yml/badge.svg)](https://github.com/Aliyas-22/github-actions-capstone/actions/workflows/main-pipeline.yml)
```
PR Opened
   ↓
CI Pipeline
   - Install dependencies
   - Run tests
   - Build Docker image
   ↓
PR Merged to main
   ↓
Push Docker image
   ↓
Deploy to Dev
   ↓
Health Check
   ↓
Deploy to Staging
   ↓
Deploy to Production
   ↓
Notifications
   ↓
Rollback (if failure)
```

