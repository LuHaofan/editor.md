from email import header
import requests
import json



headers={'content-type': 'application/json'}

def google_api(txt,api_key):
    url = "https://language.googleapis.com/v1/documents:classifyText?key="+ api_key
    json_data = {'document':{'type':'PLAIN_TEXT','content':txt}}
    payload = json.dumps(json_data)
    #payload = open('request.json')
    response = requests.post(url, data=payload,headers=headers)
    #with open("response.json","w") as f:
    #   f.write(response.text)
    print('Status code:', response.status_code)
    print(response.json())
    data = response.json()
    max_confidence = 0
    for i in data['categories']:
        if(i['confidence']>max_confidence):
            max_confidence = i['confidence']
            Category = i['name']
    print(max_confidence)
    print(Category)
    result = Category.split('/') 
    del result[0]#delete first element since it is always empty after parsing 
    result.append(max_confidence)
    print(result)
    return(result) #return result is a list of category keywords with confidence score as last element.


txt = "Backscatter communication, in which data is conveyed through reflecting excitation signals, has been advocated as a promising green technology for Internet of Things (IoT). Existing backscatter solutions however are mostly centralized, relying on a single excitation source, typically within one hop. Though recent works have demonstrated the viability of multi-hop backscatter, the excitation signal remains centralized, which attenuates quickly and fundamentally limits the communication scope. For long-range and high-quality communication, distributed excitations are expected and also naturally available as ambient signals (WiFi, BLE, cellular, FM, light, sound, etc.), albeit not being explored for boosting nearby tags for relaying.Given the existence of distributed excitation, a relay tag has to be decodable, i.e., be able to first decode its previous hop's information and then backscatter to the next hop with a boost from a nearby excitation whenever possible. In this paper, we present DecRel, a decodable tag relay solution towards a backscatter sensor mesh for universal and scalable deployment with distributed excitation. DecRel is also an innovative wireless sensor architecture for simultaneous sensing and relay. It incorporates a relay path that uses envelope detection for decoding, and a sensing path that converts its own sensor data into a baseband for amplitude-demodulation by the next hop tag's relay path. The two paths then backscatter their respective data to different frequencies to avoid interference. We have built a working DecRel tag prototype using FPGA, discrete components, and off-the-shelf analog devices. Our experiments show superior performance of DecRel as compared with the state-of-the-art non-decodable tag relay: specifically, a digital baseband's multi-hop throughput of up to 40Kbps (200x improvement), an analog baseband's equivalent multi-hop throughput of up to 768Kbps (3000x improvement), and a tag-to-tag distance of up to 4.8m (10x improvement) with a hop count of up to 6. DecRel tag consumes 337.9\u03bcW of power using IC design."
google_api(txt,AIzaSyB7sZms1ikiNAFrtAy4vjKtWcnDEl18qFM)