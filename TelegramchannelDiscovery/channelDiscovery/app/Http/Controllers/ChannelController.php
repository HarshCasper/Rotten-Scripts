<?php

namespace App\Http\Controllers;

use App\Category;
use App\Channel;
use App\Http\Requests\CreateChannelRequest;
use App\Http\Resources\ChannelResource;
use App\Photo;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class ChannelController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //get channels
        $channels = Channel::all();
        //return collection of article as a resource
        return ChannelResource::collection($channels);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $categories = Category::all();
        return view('layouts.pages.createchannel',compact('categories'));
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(CreateChannelRequest $request)
    {
        // $user = Auth::user();
        $channel = new Channel;
        $channel->user_id = $request->user_id;
        // echo($request);
        $channel->category_id = $request->cat_id;

        // $file = $request->imgurl;
        //        $photo = Photo::create(['path'=>$file]);
        //        $channel->photo_id = $photo->id;

        if ($request->hasFile('img')){
            $image = $request->file('img');
            $name = time().$image->getClientOriginalName();
            $image->move('images/channelpp',$name);
            $photo = Photo::create(['path'=>'http://localhost:8000/images/channelpp/'.$name]);
            $channel->photo_id = $photo->id;
        }else{
            echo("no file");
            return 0;
        }
        $channel->title = $request->title;
        $channel->description = $request->description;
        $channel->members = $request->members;
        $channel->contact_name = $request->contact_name;
        $channel->contact_phone = $request->contact_phone;
        $channel->contact_address = $request->contact_address;
        $channel->username = $request->username;
        $channel->save();

        // print_r($channel);

        return new ChannelResource($channel);

    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $channel = Channel::findOrFail($id);
        return new ChannelResource($channel);
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $channel = Channel::findOrFail($id);
        $categories = Category::get()->pluck('name','id')->all();
        return view('edit',compact('channel',$categories));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $channel = Channel::findOrFail($id);
        $input = $request->all();
        $channel->update($input);
        echo($id);
        print_r($input);
        // return new ChannelResource($channel);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $channel = Channel::findOrFail($id);
        unlink(public_path().$channel->photo->path);
        $channel->delete();
        return redirect('tosomething');
    }
}
