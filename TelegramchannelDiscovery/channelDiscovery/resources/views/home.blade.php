@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-3">
        <form action="{{ route('filter') }}" method="GET">

            <div class="row">
                <div class="col"> <h4 class="font-weight-bold mb-4">Filter</h4></div>
                <div class="col-md-auto"><input type="submit" class="btn btn-outline-primary rounded-0" value="Filter" onclick="filter()"></div>
            </div>
            <div class="members-count border rounded p-2">
                <strong class="">Members Count</strong><br>
                <div class="pl-3">
                    <div class="">
                        <p class="mb-0">Min(<span id="min_members_span">0</span>)</p>
                        <input type="range" min="1" max="100000" class="slider form-control-range" value="1" name="min_members" id="minrange">
                    </div>
                    <div class="">
                        <p class="mb-0">Max(<span id="max_members_span">1000000</span>)</p>
                        <input type="range" min="5000" max="1000000" value="1000000" class="slider form-control-range" name="max_members" id="maxrange">
                    </div>
                </div>
            </div>
            <div class="categories mt-4 border rounded p-2">
                <strong class="">Categories</strong>
                <div class="pl-3">
                    @foreach ($categories as $category)
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="{{$category->id}}" name="cat[]" value="{{$category->id}}">
                            <label for="{{$category->id}}">{{ $category->name }}</label><br>
                        </div>
                    @endforeach
                </div>
            </form>
            </div>
            
            
        </div>
        <div class="col-md-9">
            <h4 class="font-weight-bold mb-4">Channels</h4>
            <div class="channels card">
                @if (count($channels) > 0)
                @foreach ($channels as $channel)
                <div class="channel-item p-4 pb-0">
                    <div class="row">
                        <div class="col-md-auto">
                            <img src="{{ $channel->photo->path }}" class="rounded" alt="" width="100">
                        </div>
                        <div class="col pl-0">
                            <h5 class="font-weight-bold">{{ $channel->title }}</h5>
                            <p class="m-0">{{ $channel->description }}</p>
                            <p class="m-0 text-primary font-weight-bold">{{ $channel->members }} members</p>
                            <a class="m-0 text-primary" href="https://t.me/{{$channel->username}}" target="_blank">@ {{ $channel->username }}</a>
                        </div>
                        <div class="col-md-auto">
                            <button type="button" class="btn btn-primary" data-toggle="modal" onclick="showDesc({{$channel->id}})" data-target="#channel-desc-modal">
                                See More
                            </button>
                        </div>
                    </div>
                    <hr class="mb-0">
                </div>
                @endforeach
                @else
                <div class="channel-item p-4 pb-0">
                    <p>no result</p>
                </div>
                @endif
            </div>
        </div>
    </div>
</div>
<div class="modal fade" id="channel-desc-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content p-0 border-0">
        <div id="channel-desc-modal-content">
            <div id="scroll" class="pt-4">
                <div class="d-flex flex-column align-items-center">
                    <div class="spinner-border text-danger" role="status">
                        <span class="sr-only">Loading...</span>
                    </div>
                    <p class="text-primary">Please wait</p>
                </div>
            </div>
        </div>
        <div class="modal-footer border-0">
            <button type="button" class="btn btn-secondary" data-dismiss="modal" onclick="close()">Close</button>
        </div>
      </div>
        
    </div>
  </div>
@endsection
<script>
    function close(){
        $descContent = $("#channel-desc-modal-content");
        $descContent.html(`
            <div id="scroll" class="pt-4">
                <div class="d-flex flex-column align-items-center">
                    <div class="spinner-border text-danger" role="status">
                        <span class="sr-only">Loading...</span>
                    </div>
                    <p class="text-primary">Please wait</p>
                </div>
            </div>
        `);
    }

    function showDesc(id){
        $descContent = $("#channel-desc-modal-content");
        $.get(
            "http://127.0.0.1:8000/api/channel/"+id, (data, status)=>{
                console.log(data.data);
                console.log(status);
                if(status == 'success'){
                    $channel = data.data;
                $descContent.html(`<div class="pt-0">
                    <div class="row rounded-top bg-primary text-white pt-3 pb-3 ml-auto mr-auto" style="width:500px">
                        <div class="col-md-auto">
                            <img src="${$channel.imgurl}" class="rounded-circle" alt="" width="100">
                        </div>
                        <div class="col mt-3 ">
                            <h3><b>TIKVAH_ETH</b></h3>
                            <p class="mb-0">${$channel.members} subscribers</p>
                            <a class="m-0 text-white" href="https://t.me/@${$channel.username}" target="_blank">@ ${$channel.username}</a>
                        </div>
                    </div>
                    <div class="p-3">
                        <div>
                        <p class="font-weight-bold text-primary mb-0 pt-2 pb-1">
                            Description
                        </p>
                        <p class="mb-0">
                            ${$channel.description}
                        </p>
                    </div>
                    <div>
                        <p class="font-weight-bold text-primary mb-0 pt-2 pb-1">
                            Category
                        </p>
                        <p class="mb-0">
                            ${$channel.category}
                        </p>
                    </div>
                    <div>
                        <p class="font-weight-bold text-primary mb-0 pt-2 pb-1">
                            Contact
                        </p>
                        <div class="row pt-2">
                            <div class="col text-center">
                                <img src="{{asset('imgs/icons/person.png')}}" alt="person" width="30">
                                <p>${$channel.contact_name}</p>
                            </div>
                            <div class="col text-center">
                                <img src="{{asset('imgs/icons/phone.png')}}" alt="person" width="30">
                                <p>${$channel.contact_phone}</p>
                            </div>
                            <div class="col text-center">
                                <img src="{{asset('imgs/icons/location.png')}}" alt="person" width="30">
                                <p>${$channel.contact_address}</p>
                            </div>
                        </div>
                    </div>
                    </div>
                    </div>`);
                }
            }
        )
    }
</script>
