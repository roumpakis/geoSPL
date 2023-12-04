from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from mapHandler import mapHandler
from copernicusNotify import copernicusNotify as CN
from sentinelAPI import sentinelAPI as SAPI
from CRMAPI import CRMAPI

cn = CN()
events,feed = cn.get_all_notifications()
app = Flask(__name__)
# event_id = 'EMSN181'
# Define the IP address or hostname of the Python PC (replace with the actual IP)
python_pc_ip = 'localhost'

@app.route('/')
def index():
    # Create a Folium map and set its initial view
    mh = mapHandler(0, 0, 3,cn,True)
    mh.addLayer('openstreetmap')

    # Render the Folium map to an HTML string
    map_html = mh.m._repr_html_()

    return render_template('index.html', map_html=map_html,event_list=events)

@app.route('/get_images', methods=['GET'])
def get_images():
    print("get images called")
    # Request the images from the Python PC
    response = requests.get(f'http://{python_pc_ip}:80/get_images').json()
    return jsonify(response)

# @app.route('/event')
# def event(e):
#      print('to event')
#      # if e is None:
#      #    e = events[0]
#      event_map = SAPI.get_event_map(SAPI,e)
#      event_map_html = event_map._repr_html_()
#      event_map.save('telika.html') 
#      event_details = e['details']
     
#      return render_template('event.html', map_html=event_map_html, event_det =event_details )
@app.route('/event')
def event():
    event_id = request.args.get('event_id')
    print('event!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    if not event_id:
        return render_template('error.html', error_message='Event ID not provided')

    # Find the event with the given ID
    e = next((event for event in events if event['id'] == event_id), None)
    
    if e is None:
        return render_template('error.html', error_message='Event not found')

    # Process the event details
    event_map = SAPI.get_event_map(SAPI, e)
    event_image_before = SAPI.get_event_images_before(SAPI, e)
    event_image_after =  SAPI.get_event_images_after(SAPI, e)
    event_map_html = event_map._repr_html_()
    event_map.save('telika.html')
    
    event_details = e['details']

    return render_template('event.html', map_html=event_map_html, event_det=event_details)

@app.route('/get_event_details', methods=['POST'])
def get_event_details():
    print("get details")
    data = request.get_json()
    event_id = data.get('id')
    print("event id", event_id)
    for e in events:
        if e['id'] == event_id:
            
            print('merterere ', e["id"], e["coords"])
            break
    event_map = SAPI.get_event_map(SAPI,e)
    event_map_html = event_map._repr_html_()
    event_map.save('telika.html') 
    event_details = e['details']
    event(e)
    # print(event_details ) 
    return redirect(url_for('event', map_html=event_map_html, event_det =event_details ))

@app.route('/open_event_page', methods=['GET'])
def open_event_page():
    # Redirect to the 'event' route
    return redirect(url_for('event'))



@app.route('/rapid_mapping')
def rapid_mapping():
        rm = CRMAPI()
         # Simulated details list (replace this with your actual data)


        # Render the Folium map to an HTML string
        map_html,res_codes,res_dets =rm.get_events_map('onomataki')
        map_html = map_html._repr_html_()
        details_list =[]
        for i in range(len(res_codes)):
            details_list.append({'title': res_codes[i], 'description': res_dets[i]})
 
        return render_template('rapid_mapping.html',map_html=map_html,details_list=details_list)











@app.route('/update_input_panel', methods=['POST'])
def update_input_panel():
    print("update input called")
    # Retrieve form data
    data = request.get_json()
    print("ta data einai: ",data)
    disasters = data.get('disasters', [])
    start_date = data.get('startDate', '')
    end_date = data.get('endDate', '')
    radius = data.get('radius', '')
    print(disasters, start_date, end_date, radius)
    # Process the data as needed (e.g., pass it to the mapHandler)
    # ...

    # Redirect to the 'event' route after processing the form data
    return redirect(url_for('event'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
