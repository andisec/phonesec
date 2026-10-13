# Contributing to PhoneSec

Thank you for your interest in contributing to PhoneSec! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Step-by-step instructions
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: OS, Python version, PhoneSec version
- **Error Messages**: Any error messages or logs

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case**: Why this enhancement would be useful
- **Examples**: How it would work
- **Alternative solutions**: Other ways to achieve the same goal

### Pull Requests

1. **Fork the repository**
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**:
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise
- Comment complex logic

### Testing

- Test your changes thoroughly
- Add test cases for new features
- Ensure existing tests still pass
- Test with different phone number formats
- Test edge cases

### Documentation

- Update README.md if needed
- Add docstrings to new functions
- Update INSTALL.md for new dependencies
- Add examples for new features

## Project Structure

```
phonesec/
├── core/               # Core functionality
│   ├── phone_analyzer.py
│   ├── reporter.py
│   └── osint_links.py
├── modules/            # Additional modules
│   └── batch_analyzer.py
├── examples/           # Example scripts
├── reports/            # Generated reports (gitignored)
├── phonesec.py        # Main entry point
└── requirements.txt   # Dependencies
```

## Feature Ideas

Looking for ideas? Here are some features that could be added:

- [ ] API rate limiting for batch processing
- [ ] Database support for storing results
- [ ] Web interface
- [ ] Additional OSINT sources
- [ ] Phone number validation history
- [ ] Export to CSV/Excel
- [ ] Integration with threat intelligence feeds
- [ ] Multi-threading for batch processing
- [ ] Docker support
- [ ] CLI improvements (progress bars, better formatting)

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team.

## Questions?

Feel free to open an issue with the "question" label if you have any questions about contributing.

Thank you for contributing to PhoneSec! 🎉
