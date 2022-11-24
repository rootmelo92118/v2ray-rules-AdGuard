import os

def run():
    sourceDir = os.listdir("./data")
    exportList = ""
    for i in range(0,len(sourceDir)):
        if i == len(sourceDir)-1:
            exportList = exportList + sourceDir[i]
        else:
            exportList = exportList + sourceDir[i] + ","
    os.system("go run ./ --outputdir=./AdGuard_Rule --exportlists=" + exportList)
    print("\n\n")
    for i in sourceDir:
        with open("./AdGuard_Rule/" + i + ".txt","r") as f:
            rawData = f.readlines()
            f.close()
        processingData = []
        for rawDomain in rawData:
            processingData.append(rawDomain.strip("\n").split(":"))
        exportData = ""
        for domainData in processingData:
            if "domain" == domainData[0]:
                exportData = exportData + "||" + domainData[1] + "^\n"
            elif "full" == domainData[0]:
                exportData = exportData + "/^" + domainData[1].replace(".","\.") + "$/\n"
            elif "keywod" == domainData[0]:
                exportData = exportData + "/.+" + domainData[1] + ".+/\n"
            elif "regexp" == domainData[0]:
                exportData = exportData + "/" + domainData[1] + "/\n"
        exportData = exportData.strip("\n")
        with open("./AdGuard_Rule/" + i + ".txt","w") as f:
            f.write(exportData)
            f.close()
        print(i+" has been converted.")

    

if __name__ == '__main__':
    run()
