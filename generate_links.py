# Open a file to write the HTML
with open("index.html", "w") as f:
    # Write the beginning of the HTML document
    f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repeated Links</title>
</head>
<body>
    <h1>Links to Wasser Law MD</h1>
    <ul>
    """)

    # Generate the links 1,000,000 times
    for _ in range(1_000_000):
        f.write("""
        <li><a href="https://wasserlawmd.com/" target="_blank">Home</a></li>
        <li><a href="https://wasserlawmd.com/about/" target="_blank">About</a></li>
        <li><a href="https://wasserlawmd.com/practice-areas/" target="_blank">Practice Areas</a></li>
        <li><a href="https://wasserlawmd.com/contact/" target="_blank">Contact</a></li>
        """)

    # Close the unordered list and HTML document
    f.write("""
    </ul>
</body>
</html>
    """)

print("HTML file with 1,000,000 links created as 'index.html'")
