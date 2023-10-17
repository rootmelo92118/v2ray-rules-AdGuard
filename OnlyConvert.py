import  sys

def dataProcesser(domain_datas):
    exportData = ""
    domainNum = 0
    fullNum = 0
    keywordNum = 0
    regexpNum = 0
    for domainData in domain_datas:
        if "domain" == domainData[0]:
            exportData = exportData + "||" + domainData[1] + "^\n"
            domainNum += 1
        elif "full" == domainData[0]:
            exportData = exportData + "|" + domainData[1] + "^\n"
            fullNum += 1
        elif "keywod" == domainData[0]:
            exportData = exportData + "|*" + domainData[1] + "*^\n"
            keywordNum += 1
        elif "regexp" == domainData[0]:
            exportData = exportData + "/" + domainData[1] + "/\n"
            regexpNum += 1
    exportData = exportData.strip("\n")
    return [exportData,domainNum,fullNum,keywordNum,regexpNum]

def main(source="./faticensor.txt", output="./AdGuard_Rule"):
    with open(source,"r") as f:
        rawData = f.readlines()
        f.close()
    processingData = []
    for rawDomain in rawData:
        processingData.append(rawDomain.strip("\n").split(":"))
    exportData = dataProcesser(processingData)
    description = "# It is the censorship list of Full Access To Internet." + i + "\n" + "! domain: " + str(exportData[1]) + "\n" + "! full: " + str(exportData[2]) + "\n" + "! keyword: " + str(exportData[3]) + "\n" + "! regexp: " + str(exportData[4]) + "\n\n\n"
    with open(output + "/faticensor.txt","w") as f:
        f.write(description + exportData[0])
        f.close()
    print("All jobs have been done successfully.")

    

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
