FROM python:3
ADD calculator /calculator
RUN ls -la /calculator  # Only runs during build process
CMD ["python", "calculator/calculator.py"]