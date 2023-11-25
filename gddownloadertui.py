import gddownloadercli

gddownloader = gddownloadercli.GeometryDashDownloader(
    int(input("Enter ID: ")),
    input("Enter song name: "),
    input("Enter save path: ")
)