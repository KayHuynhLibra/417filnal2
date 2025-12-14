# Ekstazi Configuration Notes

## Current Status

The Ekstazi plugin is currently **commented out** in `pom.xml` because it requires specific JVM configuration that may not work in all environments.

## Why Commented Out?

Ekstazi uses Java agent attachment to track test dependencies. This requires:
- Proper JVM permissions
- Correct agent loading mechanism
- May not work in all CI environments without additional configuration

## How to Enable Ekstazi

1. Uncomment the Ekstazi plugin section in `pom.xml`
2. Ensure your environment supports Java agents
3. For GitHub Actions, the cache mechanism in `.github/workflows/maven.yml` will handle the `.ekstazi` directory persistence

## Alternative: Use Apache Commons CSV

For a more complete demonstration of Ekstazi, consider using the Apache Commons CSV project:

```bash
git clone https://github.com/apache/commons-csv.git
cd commons-csv
# Add Ekstazi plugin to pom.xml
mvn test
```

This project has 300+ tests and will show more dramatic time savings with RTS.

## Current Demo Project

The current project (`rts-demo`) has:
- 2 main classes: `Calculator` and `StringUtils`
- 2 test classes with 10 total tests
- All tests pass successfully
- Ready for GitHub Actions CI/CD

Even without Ekstazi enabled, this project demonstrates:
- Maven project structure
- JUnit 5 testing
- CI/CD pipeline with GitHub Actions
- Proper project organization

