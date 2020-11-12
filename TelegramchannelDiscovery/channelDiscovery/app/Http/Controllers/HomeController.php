<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Channel;
use App\Category;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $channels = Channel::all();
        $categories = Category::all();
        return view('home', compact('channels', 'categories'));
    }

    public function filter(Request $request)
    {
        if($request->input('cat') != null){
            $categories = $request->input('cat');
        }else{
            $categories = Category::all('id');
        }
        $minrange = $request->input('min_members');
        $maxrange = $request->input('max_members');
        // print($categories);
        $channels = Channel::where('members','>', $minrange)
                    ->Where('members', '<', $maxrange)
                    ->whereIn('category_id', $categories)
                    ->get();
        // echo $channels;
        $categories = Category::all();
        return view('home', compact('channels', 'categories'));
    }
}
